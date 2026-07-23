◽️[中文](#running-square-遊戲)    ◽️[English](#running-square-game)

# ***Running Square 遊戲***

## **目錄**
- [專案概述](#專案概述)
- [重點特色](#重點特色)
- [使用說明](#使用說明)
- [開發須知](#開發須知)
- [使用技術](#使用技術)
- [專案結構](#專案結構)
- [備註](#備註)


## **專案概述**
**Running Square** 是一款以 Python + Pygame 製作的 2D 橫向平台闖關遊戲。玩家操控一個方塊角色，在 15 個設計各異的關卡中穿越障礙、躲避敵人，抵達終點即可過關。


## **重點特色**
- 共 15 個手工設計的關卡，難度逐漸遞增
- 多種危險機關：靜態釘子、下落釘子、來回移動的敵人
- 動態地板：水平/垂直移動的飛行地板
- 彈簧：踩上即可獲得額外跳躍力
- 背景音樂與音效（支援靜音切換）
- 角色具備多狀態動畫（行走、靜止、閃爍、死亡）


## **使用說明**
請先下載本倉庫內容並將其解壓縮。

- **啟動**: 執行 `.exe` 檔案，如 `RunningSquare_vX.X.exe`
- **功能介紹**:

1. **移動角色**:
   - `←` / `→` 方向鍵：左右移動
   - `↑` 方向鍵：起跳（需站在地面上）
   - 踩到彈簧可獲得更高的跳躍力

2. **過關條件**:
   - 操控角色向右移動至畫面邊緣即可進入下一關
   - 共 15 關，通過第 15 關後顯示結束畫面

3. **死亡與重試**:
   - 碰到釘子、敵人，或掉出畫面底部即死亡
   - 死亡後角色自動重生於本關起點，並進入短暫無敵閃爍狀態

4. **音樂控制**:
   - 按 `ESC` 切換背景音樂靜音/恢復


## **💻開發須知**
1. 請先閱讀以下開發須知並遵守所用條款。
2. 請執行以下指令複製此倉庫至您的本地電腦:
```
cd 目標目錄
git clone https://github.com/294Ryan/RunningSquare.git
```
3. 使用語言:
   - Python 3.x

4. 安裝必要工具:
   - Python 模組：請執行以下指令
     ```
     pip install pygame
     ```

5. 使用技術: 請參見[使用技術](#使用技術)
6. 專案結構: 請參見[專案結構](#專案結構)
7. 注意：本專案代碼僅供學術研究與個人測試使用，由作者`294Ryan`保留所有權利，未獲書面授權嚴禁任何形式的商用。


## **使用技術**
- **Pygame**: 遊戲主框架，負責視窗管理、事件處理、精靈群組、遮罩碰撞偵測
- **Sprite Mask Collision (`collide_mask`)**: 以像素層級精準偵測角色與地形/敵人的碰撞
- **Hitbox 系統**: 使用四個獨立的隱形碰撞箱（上下左右）分別處理不同方向的物理行為
- **`os.walk` + `sys._MEIPASS`**: 支援 PyInstaller 打包後的資源路徑解析
- **多音效驅動自動切換**: 依序嘗試 `wasapi` → `directsound` → `dummy`，確保跨環境音效穩定性


## **專案結構**
```
RunningSquare/
├─font/
│  └─TaipeiSansTCBeta-Light.ttf
├─icons/
│  ├─icon_v1.ico
│  └─icon_v2.ico
├─image/
│  └─ *.png
├─sound/
│  └─ *.mp3 / *.wav
├─.gitignore
├─README.md
├─RunningSquare_v5.py      # 主程式進入點
└─RunningSquare_v5.spec
```


## **備註**
- 維護者: 294Ryan - [Github](https://github.com/294Ryan)
- 注意：本專案代碼僅供學術研究與個人測試使用，由作者`294Ryan`保留所有權利，未獲書面授權嚴禁任何形式的商用。
- 本專案供教育研究使用，使用時請尊重所有版權與權利擁有者。任何因不當使用造成的後果請自負。


---

# ***Running Square Game***

## **Table of Contents**
- [Overview](#overview)
- [Key Features](#key-features)
- [Usage](#usage)
- [Development Guide](#development-guide)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Notes](#notes)


## **Overview**
**Running Square** is a 2D side-scrolling platformer game built with Python and Pygame. Players control a square character through 15 uniquely designed levels, dodging obstacles and enemies to reach the goal.


## **Key Features**
- 15 handcrafted levels with progressively increasing difficulty
- Diverse hazards: static nails, falling nails, and patrolling enemies
- Dynamic platforms: horizontally and vertically moving flying grounds
- Springs: step on them for an extra boost of jump power
- Background music and sound effects (with mute toggle)
- Multi-state character animations (walking, idle, flashing, death)


## **Usage**
Download and extract the repository contents first.

- **Launch**: Run the `.exe` file, e.g. `RunningSquare_vX.X.exe`
- **Controls & Features**:

1. **Move the Character**:
   - `←` / `→` Arrow Keys: Move left/right
   - `↑` Arrow Key: Jump (must be standing on ground)
   - Land on a spring for extra jump height

2. **Clearing a Level**:
   - Move the character off the right edge of the screen to advance
   - Clear all 15 levels to reach the ending screen

3. **Death & Respawn**:
   - Touching nails, enemies, or falling off the bottom causes death
   - The character automatically respawns at the level's start with a brief invincibility flash

4. **Music Control**:
   - Press `ESC` to toggle background music on/off


## **💻Development Guide**
1. Please read the following guide and comply with the applicable license terms.
2. Clone this repository to your local machine:
```
cd target-directory
git clone https://github.com/294Ryan/RunningSquare.git
```
3. Language used:
   - Python 3.x

4. Install required dependencies:
   - Python modules: run the following command
     ```
     pip install pygame
     ```

5. Technologies Used: See [Technologies Used](#technologies-used)
6. Project Structure: See [Project Structure](#project-structure)
7. Note: This project code is for academic research and personal testing purposes only. All rights are reserved by the author `294Ryan`. Commercial use in any form is strictly prohibited without written authorization.


## **Technologies Used**
- **Pygame**: Core game framework handling windowing, event processing, sprite groups, and mask-based collision detection
- **Sprite Mask Collision (`collide_mask`)**: Pixel-perfect collision detection between the player, terrain, and enemies
- **Hitbox System**: Four independent invisible hitbox sprites (top, bottom, left, right) to handle directional physics separately
- **`os.walk` + `sys._MEIPASS`**: Resource path resolution compatible with PyInstaller-packaged executables
- **Audio Driver Auto-fallback**: Sequentially tries `wasapi` → `directsound` → `dummy` to ensure stable audio across environments


## **Project Structure**
```
RunningSquare/
├─font/
│  └─TaipeiSansTCBeta-Light.ttf
├─icons/
│  ├─icon_v1.ico
│  └─icon_v2.ico
├─image/
│  └─ *.png
├─sound/
│  └─ *.mp3 / *.wav
├─.gitignore
├─README.md
├─RunningSquare_v5.py      # main code file
└─RunningSquare_v5.spec
```


## **Notes**
- Maintainer: 294Ryan - [Github](https://github.com/294Ryan)
- Note: This project code is for academic research and personal testing purposes only. All rights are reserved by the author `294Ryan`. Commercial use in any form is strictly prohibited without written authorization.
- This project is intended for educational and research purposes. Please respect all copyrights and rights holders. Any consequences arising from improper use are solely your responsibility.
