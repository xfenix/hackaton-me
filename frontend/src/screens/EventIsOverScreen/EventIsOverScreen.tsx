import { MainLayout } from "../../components";

export const EventIsOverScreen = () => {
  return (
    <MainLayout background="">
      <h1>Мероприятие закончилось :(</h1>
      <img src={"/public/over.svg"} style={{ padding: "50px 0" }} />
    </MainLayout>
  );
};
