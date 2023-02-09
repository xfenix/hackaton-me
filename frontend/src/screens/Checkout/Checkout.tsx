import React from "react";
import { MainStoreContext } from "../../common";

export const CheckoutScreen = () => {
  const appStore = React.useContext(MainStoreContext);

  return (
    <div>
      <h1>Products</h1>
      {appStore.products.map((product) => (
        <div key={product.id}>
          <h2>{product.name}</h2>
        </div>
      ))}
      <button onClick={() => appStore.addProduct({ id: 1, name: "Product 1" })}>
        Add Product 1
      </button>
    </div>
  );
};
