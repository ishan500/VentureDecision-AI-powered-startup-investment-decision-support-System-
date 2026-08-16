export function formatCurrency(value, currency) {

    if (value === null || value === undefined) {
        return "N/A";
    }

    value = Number(value);

    if (currency === "USD") {

        if (value >= 1000) {
            return `$${(value / 1000).toFixed(1)}B`;
        }

        return `$${value}M`;
    }

    const crores = value * 8.6;

    return `₹${crores.toFixed(0)} Cr`;
}