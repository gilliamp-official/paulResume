/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./node_modules/flowbite/**/*.js',
            './mainResume/templates/**/*.html',],
  theme: {
    colors: {
      primary: '#64aaaf',
      secondary: '#335057',
      primary_text: '#F2F9F9',
    },
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

