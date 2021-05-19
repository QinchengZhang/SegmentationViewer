/*
 * @Author: TJUZQC
 * @Date: 2021-05-19 11:24:52
 * @LastEditors: TJUZQC
 * @LastEditTime: 2021-05-19 16:36:14
 * @Description: None
 */
const { ipcRender } = require('electron')
const { document } = require('globalthis/implementation')
const layui = require('./layui/layui')

document.getElementById('drag').ondragstart = (icon) => {
  event.preventDefault()
  ipcRender.send('ondragstart', 'G:\\TJUZQC\\code\\python\\SegmentationViewer\\use_electron\\viewer.ico')
}
function showMessage(msg){
  layui.use('layer', function(){
      var layer = layui.layer;
      layer.msg(msg);
  })
}