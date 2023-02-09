import { MainLayout } from "../../components";

export const EventIsOverScreen = () => {
  return (
    <MainLayout>
      <h1>Мероприятие закончилось :(</h1>
      <img src={"/public/over.svg"} />
    </MainLayout>
  );
};
