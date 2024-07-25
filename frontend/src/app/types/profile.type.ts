

export interface Profile {
  id: string
  name: string,
  details: {
    isMale: boolean,
    age: number
  }
}

export const GeneralProfile:Profile = {
  id: "",
  name: "General",
  details: {
    isMale: false,
    age: NaN
  }
}
