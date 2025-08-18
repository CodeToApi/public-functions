export function convertCurrency(amount, from, to) {
  const rates = {
    USD: 1,
    INR: 83,
    EUR: 0.91
  };

  if (!rates[from] || !rates[to]) {
    throw new Error("Unsupported currency");
  }

  return (amount / rates[from]) * rates[to];
}