import * as zod from "zod";

const ProductSchema = zod.object({
  id: zod.number(),
  name: zod.string(),
});
export type ProductType = zod.infer<typeof ProductSchema>;
