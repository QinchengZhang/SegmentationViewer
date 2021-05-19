/*
 * @Author: TJUZQC
 * @Date: 2021-05-19 11:02:25
 * @LastEditors: TJUZQC
 * @LastEditTime: 2021-05-19 11:02:25
 * @Description: None
 */
window.addEventListener('DOMContentLoaded', () => {
    const replaceText = (selector, text) => {
      const element = document.getElementById(selector)
      if (element) element.innerText = text
    }
  
    for (const type of ['chrome', 'node', 'electron']) {
      replaceText(`${type}-version`, process.versions[type])
    }
  })