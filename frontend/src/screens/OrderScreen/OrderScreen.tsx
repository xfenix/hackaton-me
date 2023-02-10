import { MainLayout } from "../../components";
import React from "react";
import { useParams } from "react-router-dom";
import * as settings from "../../common/settings";

export const OrderScreen = () => {
  const { uuidFromUrl } = useParams();
  const [serverState, setServerData] = React.useState<{
    name: string;
    description: string;
    price: number;
    logo: string;
    background: string;
    phone: string;
    email: string;
    tickets_count: number;
  }>({
    name: "",
    description: "",
    price: 0,
    logo: "",
    background: "",
    phone: "",
    email: "",
    tickets_count: 0,
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
        // window.location.href = "/404/";
      });
  }, []);

  return (
    <MainLayout background={serverState.background} logo={serverState.logo}>
      <h3>
        {serverState.tickets_count > 1 ? "Ваши билеты" : "Ваш билет"} на
        мероприятие «{serverState.name}»
      </h3>
      <p>{serverState.description}</p>
      Haha loh
    </MainLayout>
  );
};
