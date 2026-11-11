"""Contrôles de structure du kit TD3, exécutables sans navigateur ni dépendance."""
from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / 'td3'

class Structure(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags=[]
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag,dict(attrs)))

def parsed(name):
    h=Structure()
    h.feed((KIT/name).read_text(encoding='utf-8'))
    return h.tags

class TestTD3(unittest.TestCase):
    def test_manifest_and_student_documentation(self):
        for name in ['README.md','rapport-td3.md','but-boutique.html','frise-web.html',
                     'css/boutique.css','css/frise.css','js/aide-selecteur.js','images/mug.svg']:
            self.assertTrue((KIT/name).is_file(),name)
        guide=(KIT/'README.md').read_text(encoding='utf-8')
        self.assertTrue(all(key in guide for key in ['Private','Enquête 1','Enquête 2',
                        'Enquête 3','Enquête 4','rapport-td3.md']))
        self.assertIn('2 heures',guide)
        self.assertIn('au moins six diagnostics',guide)

    def test_boutique_three_products_original_core_untouched(self):
        tags=parsed('but-boutique.html')
        products=[attrs for tag,attrs in tags if tag=='article' and 'produit' in attrs.get('class','').split()]
        self.assertEqual(len(products),3)
        self.assertEqual(len([p for p in products if p.get('id')=='promo']),1)
        self.assertEqual({p.get('data-reference') for p in products},{'P01','P03','P05'})
        self.assertTrue(any(tag=='link' and attrs.get('href')=='css/boutique.css' for tag,attrs in tags))
        for tag,attrs in tags:
            if tag in ('link','script','img'):
                path=attrs.get('href') if tag=='link' else attrs.get('src')
                if path and not path.startswith('http'):
                    self.assertTrue((KIT/path).is_file(),path)
        html=(KIT/'but-boutique.html').read_text(encoding='utf-8')
        self.assertIn('12,50 €',html)
        self.assertIn('25,00 €',html)
        self.assertIn('frise-web.html',html)

    def test_timeline_preserves_historical_scope_and_selector_helper(self):
        tags=parsed('frise-web.html')
        events=[attrs for tag,attrs in tags if tag=='li' and 'evenement' in attrs.get('class','').split()]
        self.assertEqual(len(events),7)
        self.assertEqual([e.get('id') for e in events],
            ['web-1989','web-1993','web-1995','web-1996','web-2001','web-2003','web-2005'])
        self.assertEqual(sum('evenement--publication' in e.get('class','') for e in events),2)
        self.assertEqual(sum('evenement--jalon' in e.get('class','') for e in events),2)
        self.assertTrue(any(tag=='script' and a.get('src')=='js/aide-selecteur.js' for tag,a in tags))
        self.assertTrue(any(tag=='link' and a.get('href')=='css/frise.css' for tag,a in tags))
        self.assertTrue(any('data-aide-selecteur' in a for tag,a in tags))
        for tag,attrs in tags:
            if tag in ('link','script'):
                path=attrs.get('href') or attrs.get('src')
                if path and not path.startswith('http'):
                    self.assertTrue((KIT/path).is_file(),path)

    def test_css_and_aide_are_separate_and_not_inline(self):
        for page in ['but-boutique.html','frise-web.html']:
            tags=parsed(page)
            self.assertFalse(any(tag=='style' for tag,_ in tags),page)
            self.assertFalse(any('style' in attrs for tag,attrs in tags),page)
        for css in ['css/boutique.css','css/frise.css']:
            text=(KIT/css).read_text(encoding='utf-8')
            self.assertIn('@media',text)
            self.assertIn(':focus-visible',text)
        helper=(KIT/'js/aide-selecteur.js').read_text(encoding='utf-8')
        self.assertIn('querySelectorAll',helper)
        self.assertIn('textContent',helper)
        self.assertNotIn('innerHTML',helper)

if __name__=='__main__':
    unittest.main()
