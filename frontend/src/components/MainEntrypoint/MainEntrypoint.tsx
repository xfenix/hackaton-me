import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { AppMainStore, MainStoreContext } from "../../common";
import { StartScreen } from "../../screens";

const storeValue = new AppMainStore();
export const MainEntrypoint = () => {
  return (
    <Router>
      <MainStoreContext.Provider value={storeValue}>
        <Routes>
          <Route path="/" element={<StartScreen />} />
        </Routes>
      </MainStoreContext.Provider>
    </Router>
  );
};
