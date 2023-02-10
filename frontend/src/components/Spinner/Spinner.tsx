import styled from "styled-components";

const SpinnerWrapper = styled.img`
  width: 100px;
  align-self: center;
  padding: 100px 0;
`;

export const Spinner = () => {
  return <SpinnerWrapper src={"/public/spinner.svg"} />;
};
