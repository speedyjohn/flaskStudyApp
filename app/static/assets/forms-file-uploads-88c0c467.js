import"./app-22784e3d.js";import{D as n,a as p}from"./dropify.min-7eced412.js";(function(e){var o=function(){this.$body=e("body")};o.prototype.init=function(){p.autoDiscover=!1,e('[data-plugin="dropzone"]').each(function(){var t=e(this).attr("action"),r=e(this).data("previewsContainer"),i={url:t};r&&(i.previewsContainer=r);var a=e(this).data("uploadPreviewTemplate");a&&(i.previewTemplate=e(a).html()),e(this).dropzone(i)})},e.FileUpload=new o,e.FileUpload.Constructor=o})(window.jQuery),function(e){e.FileUpload.init()}(window.jQuery);$('[data-plugins="dropify"]').length>0&&new n($('[data-plugins="dropify"]'),{messages:{default:"Drag and drop a file here or click",replace:"Drag and drop or click to replace",remove:"Remove",error:"Ooops, something wrong appended."},error:{fileSize:"The file size is too big (1M max)."}});
