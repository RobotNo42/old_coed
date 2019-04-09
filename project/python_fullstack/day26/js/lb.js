  //自动轮播
    var ID = setInterval(move_right,3000);
    var i =0;
    var pic_length =$(".total .ul li").length;
    function move_right() {
        if(i==pic_length-1){
            i=-1;
        }
        i++;
        $(".total .ul li").eq(i).fadeIn(300).siblings().fadeOut(300);
        $(".total .circle_ul li").eq(i).addClass("active").siblings().removeClass("active");
    }
    function move_left(){
         if(i==-1){
            i=7;
        }
        i--;
        $(".total .ul li").eq(i).fadeIn(300).siblings().fadeOut(300);
        $(".total .circle_ul li").eq(i).addClass("active").siblings().removeClass("active");
    }
    //手动轮播
      $(".total").hover(
        function () {
            $(".bot").show();
            clearInterval(ID)

        },
        function () {
            $(".bot").hide();
            ID = setInterval(move_right,2000);
        }
    );
    $(".total .circle_ul li").mouseover(function () {
         i = $(this).index();
         $(".total .ul li").eq(i).fadeIn(300).siblings().fadeOut(300);
         $(".total .circle_ul li").eq(i).addClass("active").siblings().removeClass("active");
    });
    $(".right").click(move_right);
    $(".left").click(move_left);