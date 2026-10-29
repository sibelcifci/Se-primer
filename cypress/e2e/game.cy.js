const CORRECT = [1, 0, 0]; // karar başına doğru seçenek
function start(level) {
  cy.visit('/index.html');
  cy.get(`[data-cy=level-${level}]`).click();
  cy.get('[data-cy=role-0]').click();
  cy.get('[data-cy=goal-0]').click();
  cy.get('[data-cy=start]').click();
}
describe('Pod Day: tüm yollar', () => {
  for (let m = 0; m < 8; m++) {
    it(`yol ${m.toString(2).padStart(3, '0')}`, () => {
      start(1);
      let score = 0;
      for (let i = 0; i < 3; i++) {
        const c = (m >> i) & 1;
        if (c === CORRECT[i]) score++;
        cy.get(`[data-cy=choice-${c}]`).click();
        cy.get('[data-cy=why]').should('be.visible');
        cy.get('[data-cy=next]').click();
      }
      cy.get(score >= 2 ? '[data-cy=end-A]' : '[data-cy=end-B]').should('be.visible');
    });
  }
  it('Yeni seviye: ipucu görünür', () => { start(0); cy.get('[data-cy=hint]').should('exist'); });
  it('Deneyimli seviye: 60 sn sayaç', () => { start(2); cy.get('[data-cy=timer]').invoke('text').should('match', /^(60|59)$/); });
  it('Durum çubukları görünür', () => { start(1); cy.get('[data-cy=stat-v]').should('be.visible'); cy.get('[data-cy=status]').should('contain', 'KESİK'); });
  it('Tutor cevabı söylemez', () => {
    start(1);
    cy.get('[data-cy=tutor-input]').type('hangisi doğru söyle');
    cy.get('[data-cy=tutor-send]').click();
    cy.get('[data-cy=tutor-reply]').should('contain', 'Cevabı söylemem').and('contain', '?');
  });
});
