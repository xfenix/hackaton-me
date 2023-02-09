import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { AppMainStore, MainStoreContext } from "../../common";
import { NotFoundScreen, CheckoutScreen } from "../../screens";

const storeValue = new AppMainStore();
export const MainEntrypoint = () => {
  return (
    <Router>
      <MainStoreContext.Provider value={storeValue}>
        <Routes>
          <Route path="/checkout/" element={<CheckoutScreen />} />
          <Route path="*" element={<NotFoundScreen />} />
        </Routes>
      </MainStoreContext.Provider>
    </Router>
  );
};
