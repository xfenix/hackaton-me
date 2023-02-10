import styled from "styled-components";
import * as settings from "../../common/settings";

const SpinnerWrapper = styled.img`
  width: 100px;
  align-self: center;
  padding: 100px 0;
`;

export const Spinner = () => {
  return <SpinnerWrapper src={"/public/spinner.svg"} />;
};
