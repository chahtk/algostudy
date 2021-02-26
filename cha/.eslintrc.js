const OS = require("os");

module.exports = {
  env: {
    es6: true,
  },
  parserOptions: {
    ecmaVersion: 2018,
  },
  extends: ["airbnb-base", "plugin:prettier/recommended"],
  rules: {
    "prefer-const": 0,
    "prefer-destructuring": 0,
    "no-console": 0,
    "consistent-return": 0,
    "no-unused-vars": 0,
    "no-param-reassign": 0,
    "no-constant-condition": 0,
    "array-callback-return": 0,
    "no-continue": 0,
    "linebreak-style": ["error", OS.EOL === "\r\n" ? "windows" : "unix"],
    "prettier/prettier": ["error", { endOfLine: "auto" }],
  },
  ignorePatterns: ["node_modules/"],
};
