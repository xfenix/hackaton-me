import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { AppMainStore, MainStoreContext } from "../../common";
import {
  NotFoundScreen,
  CheckoutScreen,
  EventIsOverScreen,
} from "../../screens";

const storeValue = new AppMainStore();
export const MainEntrypoint = () => {
  return (
    <Router>
      <MainStoreContext.Provider value={storeValue}>
        <Routes>
          <Route path="/checkout/:alias" element={<CheckoutScreen />} />
          <Route path="/" element={<CheckoutScreen />} />
          <Route path="/over" element={<EventIsOverScreen />} />
          <Route path="*" element={<NotFoundScreen />} />
        </Routes>
      </MainStoreContext.Provider>
    </Router>
  );
};
