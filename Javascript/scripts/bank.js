/**
 *
 * @param {*} capital
 * @param {*} interest
 * @param {*} ages
 *
 * Se coloca una capital (c), a un interes (que se coloca entre 0 y 100), durante N años y se desea saber
 * en cuanto se ha convertido ese capital en N años. Sabiendo que el interes se acumula sobre el capital por año.
 */

function calculateCapital(capital, interest, years) {
	if (interest <= 0.0 && interest > 100) return null;
  for (let i = 1; i <= years; i++) {
		capital = (capital * interest) + capital;
  }
	return capital;
}