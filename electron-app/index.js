const path=require('path');
const {app ,BrowserWindow}=require("electron");
function createWindow(){
	const mainWindow=new BrowserWindow({
	  	title: 'test',
		width:500,
		height:700		 
	});

	//mainWindow.setIcon(null);
	mainWindow.removeMenu();
	mainWindow.loadFile(path.join(__dirname,'./renderer/index.html'));
}
app.whenReady().then(()=>{
createWindow();
}
);
