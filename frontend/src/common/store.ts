import { makeAutoObservable } from "mobx";
import { ProductType } from "./schemas";

export class AppMainStore {
  products: ProductType[] = [];

  constructor() {
    makeAutoObservable(this);
  }

  addProduct(product: ProductType) {
    this.products.push(product);
  }
}
