import { MainLayout } from "../../components";

export const NotFoundScreen = () => {
  return (
    <MainLayout background="">
      <img src={"/public/404.svg"} style={{ padding: "100px 0" }} />
    </MainLayout>
  );
};
