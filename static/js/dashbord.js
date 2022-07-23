
function player_url_update(url,title,views,transcode_status){

    var lastIndex = url.lastIndexOf("/");
    url = url.substring(0, lastIndex);
    if(transcode_status==1){
        document.getElementById('video_player_block').innerHTML = '<video id="videoPlayer" controls ></video>';  
        let video_url = "https://spext-global-cdn.staytools.com/"+url+"/result/output_manifest.mpd";
        var player = dashjs.MediaPlayer().create();
        player.initialize(document.querySelector("#videoPlayer"), video_url, true);
    }else{
        document.getElementById('video_player_block').innerHTML = '<div style="width: 600px; height: 330px; background-color: #EDE8DA;"><h2 style=" position: absolute; top: auto;">Video Processing ...</h2></div>';  
    }

    document.getElementById('video_title').innerHTML=title;
    document.getElementById('views').innerHTML=views+" Views";
}