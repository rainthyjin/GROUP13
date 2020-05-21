// pages/result/result.js
var util = require('../../util/util.js');
var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
  predict:[],
  predict1:[],
  },

  return:function(){
    wx.switchTab({
      url: '../predict/predict'
    });
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.setData({
      predict: app.globalData.predict,
      //predict1: app.globalData.predict1
      
    })
    let counts = (arr, value) => arr.reduce((a, v) => v === value ? a + 1 : a + 0, 0);
    console.log(counts(this.data.predict,0));
    console.log(app.globalData.normal);
    console.log(app.globalData.error);
  },
 
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})