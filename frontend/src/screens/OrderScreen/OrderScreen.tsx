import { MainLayout } from "../../components";
import React from "react";
import { useParams } from "react-router-dom";
import * as settings from "../../common/settings";

export const OrderScreen = () => {
  const uuidFromUrl = useParams();
  const [serverState, setServerData] = React.useState<{
    name: string;
    description: string;
    price: number;
    logo: string;
    background: string;
  }>({
    name: "",
    description: "",
    price: 0,
    logo: "",
    background: "",
  });

  React.useEffect(() => {
    // fetch data from server via fetch api
    fetch(`${settings.API_FINISH_ORDER}/${uuidFromUrl}/`)
      .then((response) => response.json())
      .then((data) => {
        setServerData(data);
      })
      .catch((error) => {
        console.log(error);
        window.location.href = "/404/";
      });
  }, []);
  return <MainLayout background="">Zdraste</MainLayout>;
};
