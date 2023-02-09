import { MainLayout } from "../../components/MainLayout";
import styled from "styled-components";
import * as settings from "../../common/settings";

export const FormWrapper = styled.form`
  margin-top: 32px;

  & label > span {
    padding-bottom: 12px;
    margin-left: 20px;
    display: block;
  }

  & input {
    display: block;
    width: 100%;
    background: #ffffff;
    border: 1px solid ${settings.COLOR_VERY_LIGHT_GRAY};
    border-radius: 8px;
    padding: 14px 20px;
    box-sizing: border-box;
    outline: none;
  }
`;
export const FormRow = styled.div``;
export const FormSeprator = styled.div``;

export const CheckoutScreen = () => {
  return (
    <MainLayout logo="ontico" background="party1">
      <h3>Конференция HighLoad</h3>
      <p>
        Крупнейшая профессиональная конференция для разработчиков
        высоконагруженных систем и их мамок, хахахаа будет гачи
      </p>
      <FormWrapper action="">
        <FormRow>
          <label>
            <span>Email:</span>
            <input type="email" name="email" placeholder="Ваш email" />
          </label>
        </FormRow>
        <FormSeprator>Или</FormSeprator>
        <FormRow>
          <label>
            <span>Телефон:</span>
            <input type="tel" name="phone" placeholder="Ваш телефон" />
          </label>
        </FormRow>
      </FormWrapper>
    </MainLayout>
  );
};
