(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-c1550d1c"],{3772:function(t,e,n){},"4ec3":function(t,e,n){"use strict";n.d(e,"D",(function(){return c})),n.d(e,"G",(function(){return o})),n.d(e,"k",(function(){return u})),n.d(e,"j",(function(){return s})),n.d(e,"E",(function(){return l})),n.d(e,"q",(function(){return d})),n.d(e,"v",(function(){return f})),n.d(e,"d",(function(){return p})),n.d(e,"F",(function(){return b})),n.d(e,"x",(function(){return g})),n.d(e,"M",(function(){return m})),n.d(e,"h",(function(){return h})),n.d(e,"g",(function(){return v})),n.d(e,"i",(function(){return _})),n.d(e,"C",(function(){return w})),n.d(e,"p",(function(){return z})),n.d(e,"u",(function(){return x})),n.d(e,"c",(function(){return k})),n.d(e,"L",(function(){return C})),n.d(e,"S",(function(){return D})),n.d(e,"s",(function(){return j})),n.d(e,"f",(function(){return y})),n.d(e,"A",(function(){return V})),n.d(e,"V",(function(){return $})),n.d(e,"O",(function(){return S})),n.d(e,"B",(function(){return O})),n.d(e,"R",(function(){return E})),n.d(e,"r",(function(){return A})),n.d(e,"l",(function(){return J})),n.d(e,"Q",(function(){return R})),n.d(e,"e",(function(){return T})),n.d(e,"N",(function(){return q})),n.d(e,"z",(function(){return B})),n.d(e,"U",(function(){return F})),n.d(e,"K",(function(){return G})),n.d(e,"H",(function(){return H})),n.d(e,"I",(function(){return I})),n.d(e,"J",(function(){return K})),n.d(e,"m",(function(){return L})),n.d(e,"n",(function(){return M})),n.d(e,"a",(function(){return N})),n.d(e,"y",(function(){return P})),n.d(e,"T",(function(){return Q})),n.d(e,"w",(function(){return U})),n.d(e,"o",(function(){return W})),n.d(e,"t",(function(){return X})),n.d(e,"b",(function(){return Y})),n.d(e,"P",(function(){return Z}));var r=n("bc3a"),a=n.n(r),i="http://127.0.0.1:9000",c=function(t){return a.a.post("".concat(i,"/user/login/"),t)},o=function(t){return a.a.post("".concat(i,"/user/register/"),t)},u=function(t){return a.a.get("".concat(i,"/user/")+t+"/count/")},s=function(t){return a.a.get("".concat(i,"/user/")+t+"/count/")},l=function(t){return a.a.get("".concat(i,"/projects/?page=")+t.page+"&size="+t.size)},d=function(t){return a.a.delete("".concat(i,"/projects/")+t+"/")},f=function(t,e){return a.a.put("".concat(i,"/projects/")+t+"/",e)},p=function(t){return a.a.post("".concat(i,"/projects/"),t)},b=function(){return a.a.get("".concat(i,"/projects/names/"))},g=function(){return a.a.get("".concat(i,"/envs/names/"))},m=function(t,e){return a.a.post("".concat(i,"/projects/")+t+"/run/",{env_id:e})},h=function(t){return a.a.get("".concat(i,"/debugtalks/?page=")+t.page+"&size="+t.size)},v=function(t){return a.a.get("".concat(i,"/debugtalks/")+t+"/")},_=function(t,e){return a.a.put("".concat(i,"/debugtalks/")+t+"/",{debugtalk:e})},w=function(t){return a.a.get("".concat(i,"/interfaces/?page=")+t.page+"&size="+t.size)},z=function(t){return a.a.delete("".concat(i,"/interfaces/")+t+"/")},x=function(t,e){return a.a.put("".concat(i,"/interfaces/")+t+"/",e)},k=function(t){return a.a.post("".concat(i,"/interfaces/"),t)},C=function(t,e){return a.a.post("".concat(i,"/interfaces/")+t+"/run/",{env_id:e})},D=function(t){return a.a.get("".concat(i,"/testsuits/?page=")+t.page+"&size="+t.size)},j=function(t){return a.a.delete("".concat(i,"/testsuits/")+t+"/")},y=function(t){return a.a.post("".concat(i,"/testsuits/"),t)},V=function(t){return a.a.get("".concat(i,"/testsuits/")+t+"/")},$=function(t,e){return a.a.put("".concat(i,"/testsuits/")+t+"/",e)},S=function(t,e){return a.a.post("".concat(i,"/testsuits/")+t+"/run/",{env_id:e})},O=function(t){return a.a.get("".concat(i,"/projects/")+t+"/interfaces/")},E=function(t){return a.a.get("".concat(i,"/testcases/?page=")+t.page+"&size="+t.size)},A=function(t){return a.a.delete("".concat(i,"/testcases/")+t+"/")},J=function(t){return a.a.get("".concat(i,"/interfaces/")+t+"/configs/")},R=function(t){return a.a.get("".concat(i,"/interfaces/")+t+"/testcases/")},T=function(t){return a.a.post("".concat(i,"/testcases/"),t)},q=function(t,e){return a.a.post("".concat(i,"/testcases/")+t+"/run/",{env_id:e})},B=function(t){return a.a.get("".concat(i,"/testcases/")+t+"/")},F=function(t,e){return a.a.put("".concat(i,"/testcases/")+t+"/",e)},G=function(t){return a.a.get("".concat(i,"/reports/?page=")+t.page+"&size="+t.size)},H=function(t){return a.a.delete("".concat(i,"/reports/")+t+"/")},I=function(t){return a.a.get("".concat(i,"/reports/")+t+"/download/",{responseType:"blob"})},K=function(t){return a.a.get("".concat(i,"/reports/")+t+"/")},L=function(t){return a.a.get("".concat(i,"/configures/?page=")+t.page+"&size="+t.size)},M=function(t){return a.a.delete("".concat(i,"/configures/")+t+"/")},N=function(t){return a.a.post("".concat(i,"/configures/"),t)},P=function(t){return a.a.get("".concat(i,"/configures/")+t+"/")},Q=function(t,e){return a.a.put("".concat(i,"/configures/")+t+"/",e)},U=function(t){return a.a.get("".concat(i,"/envs/?page=")+t.page+"&size="+t.size)},W=function(t){return a.a.delete("".concat(i,"/envs/")+t+"/")},X=function(t,e){return a.a.put("".concat(i,"/envs/")+t+"/",e)},Y=function(t){return a.a.post("".concat(i,"/envs/"),t)},Z=function(){return a.a.get("".concat(i,"/summary/"))}},c7b8:function(t,e,n){"use strict";var r=n("3772"),a=n.n(r);a.a},e8d9:function(t,e,n){"use strict";n.r(e);var r=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"table"},[n("div",{staticClass:"crumbs"},[n("el-breadcrumb",{attrs:{separator:"/"}},[n("el-breadcrumb-item",[n("i",{staticClass:"el-icon-lx-calendar"}),t._v(" 环境管理")]),n("el-breadcrumb-item",[t._v("环境列表")])],1)],1),n("div",{staticClass:"container"},[n("div",{staticClass:"handle-box"},[n("el-button",{staticClass:"handle-del mr10",attrs:{type:"primary",icon:"el-icon-delete"},on:{click:t.delAll}},[t._v("批量删除")]),n("el-input",{staticClass:"handle-input mr10",attrs:{placeholder:"输入筛选关键词"},model:{value:t.select_word,callback:function(e){t.select_word=e},expression:"select_word"}})],1),n("el-table",{ref:"multipleTable",staticClass:"table",attrs:{data:t.data,border:"",stripe:""},on:{"selection-change":t.handleSelectionChange}},[n("el-table-column",{attrs:{type:"selection",width:"55",align:"center"}}),n("el-table-column",{attrs:{type:"index",label:"序号",width:"55",align:"center"}}),n("el-table-column",{attrs:{prop:"name",label:"环境名称",width:"200"}}),n("el-table-column",{attrs:{prop:"base_url",label:"base_url",width:"350",align:"center"}}),n("el-table-column",{attrs:{prop:"desc",label:"描述",width:"200"}}),n("el-table-column",{attrs:{prop:"create_time",label:"创建时间",sortable:"",align:"center"}}),n("el-table-column",{attrs:{label:"操作",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){return[n("el-button",{attrs:{type:"text",icon:"el-icon-edit"},on:{click:function(n){return t.handleEdit(e.$index,e.row)}}},[t._v("编辑")]),n("el-button",{staticClass:"red",attrs:{type:"text",icon:"el-icon-delete"},on:{click:function(n){return t.handleDelete(e.$index,e.row)}}},[t._v("删除")])]}}])})],1),n("div",{staticClass:"pagination"},[n("el-pagination",{attrs:{background:"","page-sizes":[4,5,8,10,20],layout:"total, sizes, prev, pager, next, jumper",total:t.total_nums,"page-size":t.page_size},on:{"current-change":t.handleCurrentChange,"size-change":t.handleSizeChange}})],1)],1),n("el-dialog",{attrs:{title:"编辑环境",visible:t.editVisible,width:"35%",center:""},on:{"update:visible":function(e){t.editVisible=e}}},[n("el-form",{ref:"form",attrs:{model:t.form,"label-width":"120px"}},[n("el-form-item",{attrs:{label:"接口名称"}},[n("el-input",{attrs:{clearable:""},model:{value:t.form.name,callback:function(e){t.$set(t.form,"name",e)},expression:"form.name"}})],1),n("el-form-item",{attrs:{label:"base_url"}},[n("el-input",{attrs:{clearable:""},model:{value:t.form.base_url,callback:function(e){t.$set(t.form,"base_url",e)},expression:"form.base_url"}})],1),n("el-form-item",{attrs:{label:"简要描述"}},[n("el-input",{attrs:{clearable:""},model:{value:t.form.desc,callback:function(e){t.$set(t.form,"desc",e)},expression:"form.desc"}})],1)],1),n("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[n("el-button",{on:{click:function(e){t.editVisible=!1}}},[t._v("取 消")]),n("el-button",{attrs:{type:"primary"},on:{click:t.saveEdit}},[t._v("确 定")])],1)],1),n("el-dialog",{attrs:{title:"删除环境",visible:t.delVisible,width:"300px",center:""},on:{"update:visible":function(e){t.delVisible=e}}},[n("div",{staticClass:"del-dialog-cnt"},[t._v("删除不可恢复，是否确定删除？")]),n("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[n("el-button",{on:{click:function(e){t.delVisible=!1}}},[t._v("取 消")]),n("el-button",{attrs:{type:"primary"},on:{click:t.deleteRow}},[t._v("确 定")])],1)])],1)},a=[],i=(n("7f7f"),n("4ec3")),c={name:"basetable",data:function(){return{tableData:[],cur_page:1,page_size:10,total_nums:1,multipleSelection:[],select_word:"",del_list:[],editVisible:!1,delVisible:!1,runVisible:!1,form:{},project_idx:-1,project_id:-1,idx:-1,id:-1}},created:function(){this.getData()},computed:{data:function(){var t=this;return this.tableData.filter((function(e){for(var n=!1,r=0;r<t.del_list.length;r++)if(e.name===t.del_list[r].name){n=!0;break}if(!n&&(e.name.indexOf(t.select_word)>-1||e.desc.indexOf(t.select_word)>-1||e.base_url.indexOf(t.select_word)>-1))return e}))}},methods:{handleCurrentChange:function(t){this.cur_page=t,this.getData()},handleSizeChange:function(t){this.page_size=t,this.getData()},getData:function(){var t=this;Object(i["w"])({page:this.cur_page,size:this.page_size}).then((function(e){t.tableData=e.data.results,t.cur_page=e.data.current_page_num||1,t.total_nums=e.data.count||1}))},handleEdit:function(t,e){this.idx=t,this.id=e.id,this.form=e,this.editVisible=!0},handleDelete:function(t,e){this.idx=t,this.id=e.id,this.delVisible=!0},delAll:function(){var t=this,e=this.multipleSelection.length,n="";this.del_list=this.del_list.concat(this.multipleSelection);for(var r=0;r<e;r++)n+=this.multipleSelection[r].name+" ",Object(i["o"])(this.multipleSelection[r].id).then((function(t){})).catch((function(e){t.$message.error("服务器错误")}));this.$message.error("删除了"+n),this.multipleSelection=[]},handleSelectionChange:function(t){this.multipleSelection=t},saveEdit:function(){var t=this,e=Object.assign({},this.form);delete e.project,Object(i["t"])(this.id,e).then((function(e){if(t.editVisible=!1,t.$message.success("修改【 ".concat(t.form.name," 】成功")),t.tableData[t.idx].id===t.id)t.$set(t.tableData,t.idx,t.form);else for(var n=0;n<t.tableData.length;n++)if(t.tableData[n].id===t.id)return void t.$set(t.tableData,n,t.form)})).catch((function(e){t.editVisible=!1,t.$message.error("服务器错误")}))},deleteRow:function(){var t=this;Object(i["o"])(this.id).then((function(e){if(t.$message.success("删除成功"),t.delVisible=!1,t.tableData[t.idx].id===t.id)t.tableData.splice(t.idx,1);else for(var n=0;n<t.tableData.length;n++)if(t.tableData[n].id===t.id)return void t.tableData.splice(n,1)})).catch((function(e){t.$message.error("服务器错误")}))}}},o=c,u=(n("c7b8"),n("2877")),s=Object(u["a"])(o,r,a,!1,null,"f1b4ceda",null);e["default"]=s.exports}}]);