import { observer } from "mobx-react-lite";
import React from "react";
import { MainStoreContext } from "../../common";
import { StartScreenWrapper } from "./StartScreen.styles";

export const StartScreen = observer(() => {
  const appStore = React.useContext(MainStoreContext);

  return (
    <StartScreenWrapper>
      <h1>Products</h1>
      {appStore.products.map((product) => (
        <div key={product.id}>
          <h2>{product.name}</h2>
        </div>
      ))}
      <button onClick={() => appStore.addProduct({ id: 1, name: "Product 1" })}>
        Add Product 1
      </button>
    </StartScreenWrapper>
  );
});
