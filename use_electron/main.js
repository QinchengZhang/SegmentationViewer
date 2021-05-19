/*
 * @Author: TJUZQC
 * @Date: 2021-05-19 11:01:52
 * @LastEditors: TJUZQC
 * @LastEditTime: 2021-05-19 17:13:38
 * @Description: None
 */
const console = require("console");
const {
  app,
  BrowserWindow,
  ipcMain,
  dialog,
  webContents,
} = require("electron");
const path = require("path");

const isMac = process.platform === "darwin";

let mainWindow;

const filefilters = [
  { name: "Images", extensions: ["jpg", "png", "tif"] },
  { name: "Models", extensions: ["pdparams", "pdmodel"] },
  { name: "All Files", extensions: ["*"] },
];

ipcMain.on("ondragstart", (event, filePath) => {
  event.sender.startDrag({
    file: filePath,
    icon: "./viewer.ico",
  });
});

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, "preload.js"),
    },
  });
  mainWindow.loadFile("index.html");
}

app.whenReady().then(() => {
  require("./menu.js");
  createWindow();

  app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});
