/** @type {import('tailwindcss').Config} */
module.exports = {
  // purge: [],
  // darkMode: false, // or 'media' or 'class'
  content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {},
    colors: {
      transparent: 'transparent',
      current: 'currentColor',
      'base': '#EAE7DC',
      'green': '#85BA81',
      'yellow': '#F6B93B',
      'brown': '#DAD5C2',
      'red': '#E85A4F',
    },
  },
  // plugins: [require("tailwind-scrollbar")],
}
