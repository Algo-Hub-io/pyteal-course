# Modify the Counter App template to work with your app

For this tutorial, we have modified a basic version of the `create-react-app` template to support working with Pera Wallet and Algorand.

To start with, we need to clone the repository for the template.

```bash
https://github.com/Algo-Hub-io/counter-app.git
```

This will download the counter app template to our local machine.

To be able to run this counter app template. You would need Node and Node Package Manager (npm) installed. The installation guide is available in the following link:
https://radixweb.com/blog/installing-npm-and-nodejs-on-windows-and-mac

Next we open it in our code editor, you can either do this by opening the app and selecting the directory, or you can do it from the command line (if you are using visual studio code and have installed the console prompt)

```bash
cd counter-app
code .
```

In the VS Code windows, choose the "Terminal" option on the options menu and choose "New Terminal" to open a new terminal inside VS Code. Inside that terminal, we need to the following command to install dependencies and packages needed for the template to run:

```
npm install # OR npm i
```

After all dependencies and packages are installed, you can run the template using:

```
npm start
```

To update the template to use the smart contract that you deployed. In VS Code, update the code on `line 14` of the file: `src/App.js`:

```javascript
const appIndex = // <your smart contract index>;
```

Save the change and you should be able to interact with the app.
