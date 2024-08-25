/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./node_modules/flowbite/**/*.js',
            './mainResume/templates/**/*.html',],
  theme: {
    colors: {
      primary: '000000',
      secondary: '#335057',
      primary_text: '#64aaaf',
      secondary_text: '#F2F9F9',
    },
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

