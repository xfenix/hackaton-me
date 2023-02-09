export const formatPrice = (price: number) => {
  // split rubles by thousands with spaces
  return price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
};
