import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { AppMainStore, MainStoreContext } from "../../common";
import { CheckoutScreen } from "../../screens/CheckoutScreen";

const storeValue = new AppMainStore();
export const MainEntrypoint = () => {
  return (
    <Router>
      <MainStoreContext.Provider value={storeValue}>
        <Routes>
          <Route path="/" element={<CheckoutScreen />} />
        </Routes>
      </MainStoreContext.Provider>
    </Router>
  );
};
