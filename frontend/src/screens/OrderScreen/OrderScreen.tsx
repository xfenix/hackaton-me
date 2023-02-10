import { MainLayout } from "../../components";
import React from "react";
import { useParams } from "react-router-dom";
import * as settings from "../../common/settings";
import styled from "styled-components";

const EventDescription = styled.p`
  margin-bottom: 30px;
`;
const SubmittedFooterDescription = styled.p`
  margin-top: 30px;
`;
const OneBarcodeItem = styled.div`
  overflow: hidden;
  margin-top: 20px;

  & > span {
    font-size: 12px;
    color: ${settings.COLOR_LIGHT_GRAY};
  }

  & > img {
    display: block;
    width: 100%;
  }
`;
export const OrderScreen = () => {
  const { uuidFromUrl } = useParams();
  const [whereSubmitted, setWhereSubmitted] = React.useState("");
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
        window.location.href = "/404/";
      });
  }, []);
  React.useEffect(() => {
    const whereTextParts = [];
    if (serverState.email) whereTextParts.push(`email ${serverState.email}`);
    if (serverState.phone) whereTextParts.push(`телефон ${serverState.phone}`);
    setWhereSubmitted(whereTextParts.join(" и "));
  }, [serverState]);

  return (
    <MainLayout background={serverState.background} logo={serverState.logo}>
      <h3>
        {serverState.tickets_count > 1 ? "Ваши билеты" : "Ваш билет"} на
        мероприятие «{serverState.name}»
      </h3>
      <EventDescription>{serverState.description}</EventDescription>
      <div className="small-text">
        Покажите{" "}
        {serverState.tickets_count > 1 ? "любой из штрих-кодов" : "штрих-код"}
        на входе на мероприятие:
      </div>
      {[...Array(serverState.tickets_count)].map((_, oneIndex) => (
        <OneBarcodeItem key={oneIndex}>
          <img
            src={`${settings.API_PDF417_BARCODE}/${uuidFromUrl}/?ticket-number=${oneIndex}`}
            alt="Один билет на мероприятие"
          />
          {serverState.tickets_count > 1 ? (
            <span>Билет {oneIndex + 1}</span>
          ) : (
            <></>
          )}
        </OneBarcodeItem>
      ))}
      <SubmittedFooterDescription>
        Так же ссылка на эту страницу и чек отправлены на ваш {whereSubmitted}
      </SubmittedFooterDescription>
    </MainLayout>
  );
};
