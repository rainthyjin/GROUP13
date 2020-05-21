// pages/charts/charts.js
import * as echarts from '../../ec-canvas/echarts';
var app = getApp()
var initChart = null
   
  
function setOption(chart, result0,result1,result2,result3) {
      var options = {
        series: [{
          type: 'pie',
          radius: '55%',
          data:[
              {value:result0, name:'正常'},
              {value:result1, name:'Ball'},
              {value:result2, name:'内圈故障'},
              {value:result3, name:'外圈故障'}  
          ]
        }]
      }
      chart.setOption(options);
}



Page({

  /**
   * 页面的初始数据
   */
  data: {
    show:false,
    columns1:['100','108','121','133','147','160','172','188','200','212','225','237','249','261'],
    show1:false,
    result0:1,
    result1:1,
    result2:1,
    result3:1,
    time:'',
    predict:[],
    value1:'',
    ec: {
      onInit: initChart
    }
  },


  showPopup: function() {
    this.setData({show:true});
    this.setData({show1:true});
    },

    onClose:function() {
      this.setData({ show: false });
      this.setData({ show1: false });
    },

    showdata:function(value){
      let counts = (arr, value) => arr.reduce((a, v) => v === value ? a + 1 : a + 0, 0);
      switch(value) {
        case '100':
          this.setData({result0:counts(app.globalData.predict1,0),result1:counts(app.globalData.predict1,1),result2:counts(app.globalData.predict1,2),result3:counts(app.globalData.predict1,3)});
           break;
        case '108':
          this.setData({result0:counts(app.globalData.predict2,0),result1:counts(app.globalData.predict2,1),result2:counts(app.globalData.predict2,2),result3:counts(app.globalData.predict2,3)});
           break;
        case '121':
          this.setData({result0:counts(app.globalData.predict3,0),result1:counts(app.globalData.predict3,1),result2:counts(app.globalData.predict3,2),result3:counts(app.globalData.predict3,3)});
           break;
        case '133':
          this.setData({result0:counts(app.globalData.predict4,0),result1:counts(app.globalData.predict4,1),result2:counts(app.globalData.predict4,2),result3:counts(app.globalData.predict4,3)});
           break;
        case '147':
          this.setData({result0:counts(app.globalData.predict5,0),result1:counts(app.globalData.predict5,1),result2:counts(app.globalData.predict5,2),result3:counts(app.globalData.predict5,3)});
           break;
        case '160':
          this.setData({result0:counts(app.globalData.predict6,0),result1:counts(app.globalData.predict6,1),result2:counts(app.globalData.predict6,2),result3:counts(app.globalData.predict6,3)});
           break;
        case '172':
          this.setData({result0:counts(app.globalData.predict7,0),result1:counts(app.globalData.predict7,1),result2:counts(app.globalData.predict7,2),result3:counts(app.globalData.predict7,3)});
           break;
        case '188':
          this.setData({result0:counts(app.globalData.predict8,0),result1:counts(app.globalData.predict8,1),result2:counts(app.globalData.predict8,2),result3:counts(app.globalData.predict8,3)});
           break;
        case '200':
          this.setData({result0:counts(app.globalData.predict9,0),result1:counts(app.globalData.predict9,1),result2:counts(app.globalData.predict9,2),result3:counts(app.globalData.predict9,3)});
           break;
        case '212':
          this.setData({result0:counts(app.globalData.predict10,0),result1:counts(app.globalData.predict10,1),result2:counts(app.globalData.predict10,2),result3:counts(app.globalData.predict10,3)});
          break;
        case '225':
          this.setData({result0:counts(app.globalData.predict11,0),result1:counts(app.globalData.predict11,1),result2:counts(app.globalData.predict11,2),result3:counts(app.globalData.predict11,3)});
           break;
        case '237':
          this.setData({result0:counts(app.globalData.predict12,0),result1:counts(app.globalData.predict12,1),result2:counts(app.globalData.predict12,2),result3:counts(app.globalData.predict12,3)});
            break;
        case '249':
          this.setData({result0:counts(app.globalData.predict13,0),result1:counts(app.globalData.predict13,1),result2:counts(app.globalData.predict13,2),result3:counts(app.globalData.predict13,3)});
            break;
        case '261':
          this.setData({result0:counts(app.globalData.predict14,0),result1:counts(app.globalData.predict14,1),result2:counts(app.globalData.predict14,2),result3:counts(app.globalData.predict14,3)});
           break;
   } 
    },

    onConfirm1(event) {
      const { picker, value, index } = event.detail; 
      this.setData({ value1: value,time:app.globalData.time });
      this.setData({ show: false });
      this.setData({ show1: false });
      this.showdata(this.data.value1);
      this.init_one(this.data.result0,this.data.result1,this.data.result2,this.data.result3);
    },


    init_one: function (result0,result1,result2,result3) {           //初始化第一个图表
      this.oneComponent.init((canvas, width, height) => {
        const chart = echarts.init(canvas, null, {
          width: width,
          height: height
        });
        setOption(chart,result0,result1,result2,result3)  //赋值给echart图表
        this.chart = chart;
        return chart;
      });
    },
    onCancel:function() {
      // Toast('取消');
       this.setData({ show: false });
       this.setData({ show1: false });
     },
     


  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.setData({
      time: app.globalData.time,
    });
    this.oneComponent = this.selectComponent('#mychart-dom-bar');
    this.init_one(this.data.result0,this.data.result1,this.data.result2,this.data.result3);
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