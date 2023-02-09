import { createGlobalStyle } from "styled-components";

const GlobalStyle = createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
  }
`;

export const MainLayout = (props: { children: JSX.Element }) => {
  return (
    <>
      <GlobalStyle />
      <main>{props.children}</main>
    </>
  );
};
