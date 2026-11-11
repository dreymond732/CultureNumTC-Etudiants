/* TD3 — Aide-Sélecteur : surligner une sélection sans éditer les styles. */
document.addEventListener('DOMContentLoaded', () => {
  const root = document.querySelector('[data-aide-selecteur]');
  if (!root) return;
  const input = root.querySelector('#selecteur-a-tester');
  const message = root.querySelector('#resultat-selecteur');
  const clearButton = root.querySelector('#effacer-selection');
  const clearHighlight = () => {
    document.querySelectorAll('.cible-testee').forEach(node => node.classList.remove('cible-testee'));
  };
  input.addEventListener('input', () => {
    clearHighlight();
    const selector = input.value.trim();
    if (!selector) { message.textContent = 'Aucun sélecteur testé.'; return; }
    try {
      const matches = [...document.querySelectorAll(selector)].filter(node => !root.contains(node));
      matches.forEach(node => node.classList.add('cible-testee'));
      message.textContent = `${matches.length} élément(s) ciblé(s).`;
    } catch (error) {
      message.textContent = 'Sélecteur invalide : vérifiez sa syntaxe.';
    }
  });
  clearButton.addEventListener('click', () => {
    input.value = '';
    clearHighlight();
    message.textContent = 'Surlignage effacé.';
    input.focus();
  });
});
