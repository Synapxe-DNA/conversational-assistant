export interface Profile {
  id: string
  name: string
  isMale: boolean
  age: number
  existing_conditions: string
}

export const GeneralProfile: Profile = {
  id: "",
  name: "General",
  isMale: false,
  age: NaN,
  existing_conditions: "",
}
