import { MainLayout } from "../../components/MainLayout";
import { useForm } from "react-hook-form";
import styled from "styled-components";
import * as settings from "../../common/settings";
import { formatPrice } from "../../common/helpers";
import { useParams } from "react-router-dom";

const TYPICAL_PADDING = 20;
export const FormWrapper = styled.form`
  margin-top: 32px;

  & label > span {
    margin-bottom: 8px;
    margin-left: ${TYPICAL_PADDING}px;
    display: block;
  }

  & input {
    display: block;
    width: 100%;
    background: #ffffff;
    border: 1px solid ${settings.COLOR_VERY_LIGHT_GRAY};
    border-radius: 8px;
    padding: 18px ${TYPICAL_PADDING}px;
    box-sizing: border-box;
    outline: none;
  }
`;
export const FormRow = styled.div``;
export const FormSeparator = styled.div`
  color: ${settings.COLOR_LIGHT_GRAY};
  display: flex;
  align-items: center;
  gap: 16px;
  margin: 24px 0 16px 0;
  padding: 0 ${TYPICAL_PADDING}px;
  font-size: 12px;

  &::before,
  &::after {
    display: block;
    content: "";
    background: ${settings.COLOR_LIGHT_GRAY};
    height: 1px;
    width: 100%;
  }
`;
export const SubmitButton = styled.button`
  margin-top: 32px;
  background: ${settings.COLOR_BRAND};
  border-radius: 8px;
  padding: 18px ${TYPICAL_PADDING}px;
  display: flex;
  align-items: center;
  border: 1px solid ${settings.COLOR_VERY_LIGHT_GRAY};
  transition: background-color 0.4s ease;
  width: 100%;
  box-sizing: border-box;
  cursor: pointer;

  & > span {
    flex-grow: 3;
    text-align: left;
    margin-left: 12px;
  }

  &:active {
    position: relative;
    top: 1px;
  }

  &:hover {
    background: #fed500;
  }
`;

export const CheckoutScreen = () => {
  let { alias } = useParams();
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm();
  const onSubmit = (data: any) => console.log(data);
  return (
    <MainLayout logo="ontico" background="party1">
      <h3>Конференция HighLoad</h3>
      <p>
        Крупнейшая профессиональная конференция для разработчиков
        высоконагруженных систем и их мамок, хахахаа будет гачи
      </p>
      <FormWrapper action="" onSubmit={handleSubmit(onSubmit)}>
        <FormRow>
          <label>
            <span>Email:</span>
            <input
              type="email"
              placeholder="Ваш email"
              {...register("email")}
            />
          </label>
        </FormRow>
        <FormSeparator>
          <div>Или</div>
        </FormSeparator>
        <FormRow>
          <label>
            <span>Телефон:</span>
            <input
              type="tel"
              placeholder="Ваш телефон"
              {...register("phone")}
            />
          </label>
        </FormRow>
        <SubmitButton type="submit">
          <svg
            width="24"
            height="20"
            viewBox="0 0 24 20"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M16.8 10.8H19.2V8.4H16.8V10.8ZM15.6 12C14.28 12 13.2 10.92 13.2 9.6C13.2 8.28 14.28 7.2 15.6 7.2H21.6V12H15.6ZM2.4 16.8V2.4H19.2V4.8H15.6C12.948 4.8 10.8 6.948 10.8 9.6C10.8 12.252 12.948 14.4 15.6 14.4H19.2V16.8H2.4ZM1.2 19.2H20.4C21.06 19.2 21.6 18.66 21.6 18V16.8C21.6 15.636 21.012 14.868 19.992 14.556V14.4H22.8C23.46 14.4 24 13.86 24 13.2V6C24 5.34 23.46 4.8 22.8 4.8H19.992V4.644C21.012 4.332 21.6 3.564 21.6 2.4V1.2C21.6 0.54 21.06 0 20.4 0H1.2C0.54 0 0 0.54 0 1.2V18C0 18.66 0.54 19.2 1.2 19.2Z"
              fill="#2B2D33"
            />
          </svg>
          <span>Оплатить</span>
          <strong>{formatPrice(1585)} ₽</strong>
        </SubmitButton>
      </FormWrapper>
    </MainLayout>
  );
};
