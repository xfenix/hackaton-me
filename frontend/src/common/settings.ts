export const STYLE_BORDER_RADIUS = 12;
export const COLOR_BLACK = "#2B2D33";
export const COLOR_VERY_LIGHT_GRAY = "#e1e1e3";
export const COLOR_LIGHT_GRAY = "#A2A4A6";
export const COLOR_BRAND = "#FEE600";
export const COLOR_RED = "#EE505A";
export const DEFAULT_FONT_NAME = "ALS Hauss";
export const DEFAULT_BACKGROUND = "party2";
export const PNG_LOGOS = ["ontico", "pycon"];
export const GOOD_STATUS = 1;

// const BACK_API_DOMAIN = "self-service-checkout-events-back.5723.raiff2023.codenrock.com";
const BACK_API_DOMAIN = "127.0.0.1:8000";
export const BACK_API_ROOT = `http://${BACK_API_DOMAIN}/api`;
export const API_FETCH_EVENT = `${BACK_API_ROOT}/fetch-event-info`;
export const API_MAKE_ORDER = `${BACK_API_ROOT}/make-order/`;
export const API_FINISH_ORDER = `${BACK_API_ROOT}/finish-order`;
export const API_PDF417_BARCODE = `${BACK_API_ROOT}/pdf417-code`;
