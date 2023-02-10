import { MainLayout } from "../../components/MainLayout";
import { useForm } from "react-hook-form";
import styled from "styled-components";
import * as settings from "../../common/settings";
import { formatPrice } from "../../common/helpers";
import { useParams } from "react-router-dom";
import React from "react";

const TYPICAL_PADDING = 20;
const RADIO_VALUES = [1, 2, 3, 4, 5, 6];
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
export const EventDescription = styled.div`
  min-height: 100px;
`;
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
export const FormTicketsCountRow = styled.div`
  padding: 0 ${TYPICAL_PADDING}px;
  margin-bottom: 24px;

  & > span {
    display: block;
    margin-bottom: 8px;
  }

  & > div {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  & input[type="number"] {
    max-width: 120px;
    display: block;
    margin-left: 30px;
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
export const TicketRadio = styled.label<{ checked: boolean }>`
  font-size: 26px;
  line-height: 32px;
  width: 48px;
  height: 48px;
  font-weight: normal;
  border-radius: 100% !important;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  transition: background-color 0.2s ease;
  ${(props) => props.checked && `background: ${settings.COLOR_BRAND};`}

  &:hover {
    background: ${settings.COLOR_BRAND};
  }

  & > span {
    margin: 0 !important;
    margin-top: 6px !important;
    padding: 0;
  }

  & > input {
    display: none;
  }
`;

export const CheckoutScreen = () => {
  const [serverState, setServerData] = React.useState<{
    name: string;
    description: string;
    price: number;
    logo: string;
    background: string;
  }>({
    name: "",
    description: "",
    price: 0,
    logo: "",
    background: "",
  });
  let { alias } = useParams();
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
    setValue,
  } = useForm({
    defaultValues: {
      amount: "1",
      email: "",
      phone: "",
    },
  });
  const onSubmit = (data: any) => console.log(data);
  React.useEffect(() => {
    // fetch data from server via fetch api
    fetch(`${settings.BACK_API_ROOT}/fetch-event-info/${alias}/`)
      .then((response) => response.json())
      .then((data) => {
        setServerData(data);
      });
  }, []);

  return (
    <MainLayout logo={serverState.logo} background={serverState.background}>
      <h3>{serverState.name}</h3>
      <EventDescription>{serverState.description}</EventDescription>
      <FormWrapper action="" onSubmit={handleSubmit(onSubmit)}>
        <FormTicketsCountRow>
          <span className="small-text">Количество билетов:</span>
          <div>
            {RADIO_VALUES.map((oneValue) => (
              <TicketRadio
                key={oneValue}
                checked={watch("amount") === oneValue.toString()}
              >
                <span>{oneValue}</span>
                <input type="radio" value={oneValue} {...register("amount")} />
              </TicketRadio>
            ))}
            <input
              type="number"
              min={7}
              max={30}
              placeholder="8"
              onChange={(eventBody) => {
                setValue("amount", eventBody.target.value);
              }}
            />
          </div>
        </FormTicketsCountRow>
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
          <strong>
            {formatPrice(serverState.price * Number(watch("amount")))} ₽
          </strong>
        </SubmitButton>
      </FormWrapper>
    </MainLayout>
  );
};
