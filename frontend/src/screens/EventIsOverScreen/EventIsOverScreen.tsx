import { MainLayout } from "../../components";

export const EventIsOverScreen = () => {
  return (
    <MainLayout>
      <h1>Мероприятие закончилось :(</h1>
      <img src={"over.svg"} />
    </MainLayout>
  );
};
