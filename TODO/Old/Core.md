光明阵营优势在生产，发育，防守，治疗，拆塔
体现在：worker采集效率高，generator生产效率高，单位偏血量和治疗；对建筑伤害提升（不包括水晶）
但是，其convertor效率低

黑暗阵营优势在进攻，掠夺
体现在：移速高，对单位攻击力提升，convertor效率高
但是，其单位血量低，generator效率低，worker效率低，对建筑伤害降低（不包括水晶）
黑暗兵种击败敌人获取一定数量的黑暗能量。

游戏以波数为主，守护水晶，波数越多分数越高。
资源系统：大部分自然资源都是可再生资源，少部分属于植物大战僵尸的阳光那种，随机掉落地面刷新，有存在时限，玩家需要开采收集。
而建造和召唤所需的资源大部分通过生产或者转化获取。

敌人 AI 系统
我想实现以下结构的ecs rts ai：

1. 敌人的各个兵种有不同的生成间隔，基于波次和难度预先设定；
2. 敌人的ai最小管理单位是team，一个team由若干个固定个数的敌人组成，组成成分基于波次和难度预先设定；
3. team有4类，gather，attack，defense，harass。每当有一个敌方unit生成后，根据当前strategy和该unit种类和该unit属于哪个基地entity将该unit加入到指定缺人team，并令其移动到指定位置（基地内部集结地）。所有缺人team的entity存储在基地entity的4个buffer中（对应4类team）。
4. 所有种类的team在一个波次有最高上限数量，基于难度提前指定，attack team除外。这就是说，当其他3个team都已经达到上限数量时，所有后生成的兵种全部加入attack team。
5. strategy有4x3x2x1=24种，如gadh是指优先将生成的兵种加入gather team（如果其兵种种类合适，并且gather team有空缺或者gather team未达上限数量，否则下一个team），括号内的条件不满足，则加入attack team，以此类推。ahdg是最激进的策略，因为它优先加入attack。（首字母排列）
6. strategy按照波数和难度预先设定，每个波次内无论场上局势如何都不会改变（这个后面有条件改成根据当前场上局势设定，现在先完成最基础的）;
7. 所有unit有自己的状态机，这个与该ai系统无关，是其他系统实现的，只是拿过来用接口。unit有状态idle，interact（attack，heal，harvest），moving，garrison。这部分已经实现了。
8. 每个team都有他自己的状态，但所有team的状态机类似。team状态有如下几种：空闲/非空闲：当前队伍中只要有一个unit不处于idle状态就认为整个team非空闲；缺人/非缺人：当前队伍的unit数量小于指定数量的一半则缺人。
9. team的状态机：检查是否空闲，非空闲则返回不管（因为这意味着单位有目标，交给底层ai处理）。空闲时，检查是否缺人，缺人则命令其返回基地指定位置，并将该team的entity加入到基地缺人team的buffer中。不缺人，则根据当前team种类，寻找目标，并设定前往目标（前往目标只需对该team每个unit发个command指令即可，剩下的工作交给底层系统）。
10. 4类team各自的目标：gather team目标为resource，attack team目标为玩家水晶（水晶有专门的tag），defense目标为该team所属基地的可驻扎(有garrison tag)且未满员的建筑以及基地附近点位（这个只需在指定半径处随机选择一个点即可），harass team目标为当前场上不在玩家基地的采集单位（这些单位有一个监视系统，只要远离基地则会带上一个tag），以及基地附近指定半径处的随机点位。
选择目标时，有一个value系统，根据预先设定的权重，和各个目标身上的component数据，计算出value存储到其value component。目标选择时需要相对的选择一个较大value的目标。


待完成 ！！！
机制支持：

Buff system ：
范围性bufftrigger ： 通过类似sight的机制，同步一个collider与trigger，检查其碰撞到的单位，并未他们添加buff


Fog of war：
1. 光明阵营只有骑兵、信标、水晶不会hide in fog和提供视野，其他单位会hide in fog。
2. 暂时性buff似的视野：生成一个sight并同步它和目标的位置
3. 所有hide in fog的单位不再selectable；不在clickable？怎么实现？（可以先不管，当成不怎么重要的bug）
4. 当玩家阵营为光明时启动hide in fog系统，否则只是启动效果系统



对于我的光暗之战rts，我还有最后3天。游戏基本机制的积木已经全部准备好，现在缺的是将他们拼在一起。我的ecsrts支持超大地图，超多单位，地图随机生成生态群落，不同生态群落有不同的资源；敌人的生成方式是根据预设生成间隔逐渐减小，生成单位逐渐变强；敌人建筑是根据预设生成间隔逐渐减小，一次性生成一个建筑群。
游戏支持两个阵营：光明或者黑暗。兵种有5种：盾，骑，弓，魔法，采集；

敌人总AI：根据难度指定固定总波数，波的间隔是预设的（逐渐减小），敌人单位的生成随波数生成间隔减小，生成单位变多，阶级提升；

|阵营特色 |玩家方 | AI方|

|光明阵营|视野受限=光明受限，唯有骑兵（可多）、信标（可多）、水晶（唯一）周围范围内可见敌人；视野范围外玩家不可操控兵种但是兵种始终可见；|敌人没有玩家基本建筑的视野，策略偏防御，只有被某个单位看见的黑暗水晶会被打上暴露tag，被打上tag的水晶将成为attack目标。在存在目标之前，敌人只有defend队伍，采集队伍，和harass队伍，harass队伍的ai是全局随机选择一个一个位于玩家水晶周围一定范围内的随机点奔赴，用以模拟探查，随着时间增加，搜索范围将越来越小；敌人的建筑是预设的，且不会动态生成；敌人召唤的单位逻辑不变；此时波数不再显示给玩家，而只作为难度随时间提升的参考。|

|黑暗阵营|全局视野；但是黑暗兵种在强光明范围内（即光明骑兵、信标、水晶范围）会受到极大削弱（攻击力削减一半，血量减少一半）| 敌人拥有玩家所有信标和水晶的视野，策略偏进攻，harass队伍目标是暴露在基地之外的单位。敌人的建筑随波数生成，固定波数之后生成结束（随难度定制波数），每次生成都是一个建筑群，包含一个或多个黑暗水晶。玩家防守住指定波数并击毁所有黑暗水晶获取胜利。

天网： 黑暗单位在光明中属性削弱，hp上限 -30%， 移动速度减少 10%
迷失 ：光明单位在黑暗中血量逐渐减少且会丢失视野内所有目标(包括建筑)

建筑造成的伤害为魔法伤害；

兵种特色如下表：
工人兵种互相克制，骑兵互相克制；
光盾克制黑暗魔法， 黑暗盾克制光明魔法；
光弓克制黑暗盾，黑暗弓克制光明盾；
光魔法克制黑暗弓， 黑暗魔法克制光明弓；
1阶单位增益为0

| 兵种                | 光明阵营                                              | 黑暗阵营       |        
|---------------------|------------------------------------------------------|----------------------|
|盾总体特性        | 血量厚，移速低，可以阻挡水平飞行的飞行物（剑气，塔的魔法球）| |
|  盾1阶                 | 守护：附近一定数量队友受到伤害时，将伤害传导到自己身上，根据伤害类型减免受到的传递伤害  | 嘲讽：嘲讽一定数量的敌人，并根据其伤害类型反弹一定的对方造成的伤害|
| 盾2阶                | 增加传导数量，减伤比例增加                        |增加嘲讽数量，反伤比例增加|
|盾 3阶              | 增加传导数量，减伤比例增加  |增加嘲讽数量，反伤比例增加 |
|弓总特性 |血量薄， 移速中， 范围远      | |
|弓1阶| 破魔：对所有黑暗能量的造物 攻击附加百分比伤害；建筑和单位依照不同的百分比计算|毁灭：每次攻击会使箭矢分叉，对多个单位造成伤害 |
|弓2阶| 百分比伤害提升， | 分叉箭伤害提升，分叉数量提升|
|弓3阶| 百分比伤害增加| 分叉箭伤害提升，分叉数量提升|
|魔法总特性| 血量薄， 移速中， 范围中， 可攻击可治疗| |
|魔法1阶纯攻|压制： 目标行动迟缓持续一段时间（不可叠加）|腐蚀：目标受到的回复效果减弱，持续一段时间|
|魔法2阶纯攻|迟缓程度提高  |恢复效果下降程度提高，持续时间提高|
|魔法3阶纯攻| 迟缓程度提高|回复效果下降程度提高，持续时间提高|
|魔法1阶纯治疗| 拯救：单体治疗；光明魔法具有更高的治愈量|疯狂：被治疗的单位攻击力短时间提升。|
|魔法2阶纯治疗| 多单位单体治疗，具有更高的治愈量|多单位单体治疗，攻击力提升持续时间增加|
|魔法3阶纯治疗| 群体治疗，治疗量增加|群体治疗，攻击力提升|
|工人总特性| 血量低， 移速中，近战；唯一可以开采资源，进驻资源矿的单位| |
|工人1阶| 勤劳：生产效率提升| 掠夺： 转化资源效率提升|
|工人2阶 |生产效率进一步提升 |转化效率进一步提升|
|工人3阶| 生产效率提升|转化效率提升|
| 骑总体特性              | 血量中，移速快，主动攻击力中等；移动状态下受到的伤害减少| |
|  骑1阶             |领袖： 附近一定数量的单位基础属性增加；不可叠加| 强袭：自身血量越少攻击力越高。不可以与疯狂buff叠加|               
| 骑兵2阶             | 基础属性增加幅度提升 |   攻击力提升比例增加|
|骑兵3阶|基础属性增加幅度提升 | 攻击力提升比例增加|

理想状况： 光明一方先上盾，骑，弓，治疗；黑暗一方先上盾，魔法，弓，治疗；光明一方尽量让弓箭手被黑暗盾嘲讽，其他未被嘲讽的单位优先攻击黑暗治疗和黑暗法师，同时阻拦黑暗骑兵突进到光明治疗、光明法师跟前；黑暗单位则让黑暗弓箭手优先攻击光明非盾单位，通过伤害传导攻击光明盾牌；黑暗法师给光明盾牌叠加debuff减弱其回血；黑暗治疗师则提升单位各单位伤害；黑暗骑兵突进到后方自杀式袭击光明法师和光明治疗。

削弱方案：光明盾提供的减伤值减少；黑暗弓流血伤害？


# 阵营特色2.0

### 势力判别：
对于目标faction为neutral的，无论玩家什么faction，都是neutral关系
玩家Faction为Light（Ally为变量名）：faction相同时， 包含subfaction则为self，不包含则为ally；faction不同为hostile
玩家Faction为Dark（Enemy为变量名）： faction相同时，包含subfaction为self，不包含为neutral；faction不同为hostile

### Tag Component

PlayerTag添加到self 的关系上，AITag添加到其他关系上
当玩家征服一个新势力时，使用expand faction方法改变playerfactiondata，然后init distinguish system负责更新tag

ally的关系：

- 军队可以驻扎，可以通过；可以进城参观，不可以操控；
- 军队相遇时，一方进入战斗时另一方也会进入战斗；战斗过程中双方共享buff，但是玩家只能操控自己的军队
neutral的关系：
- 军队可以通过，不可以驻扎，不可以进城参观，不可以操控；
- 军队相遇时，一方进入战斗不会导致另一方进入战斗；除非一方的目标是对方
hostile的关系：
- 军队不可以通过，不可以驻扎，不可以进城
- 军队相遇时触发遭遇战


### 💂 Unit Buff Description Table (EN)

| Unit Type                    | Light Faction                                                                                               | Dark Faction                                                                       |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **Shield - General Traits**  | High HP, slow movement, zero base attack power                                                              |                                                                                    |
| **Shield Tier 1**            | Redirects damage taken by nearby allies to self; redirected damage is reduced based on damage type          | Taunts multiple enemies; reflects a portion of incoming damage based on its type   |
| **Shield Tier 2**            | Increases redirection count; increased damage reduction percentage                                          | Increases taunt count; increased damage reflection percentage                      |
| **Shield Tier 3**            | Further increases redirection count and damage reduction                                                    | Further increases taunt count and damage reflection                                |
| **Archer - General Traits**  | Low HP, medium movement speed, long range                                                                   |                                                                                    |
| **Archer Tier 1**            | Attacks deal bonus damage based on target’s max HP (cannot be reflected); special calculation for buildings | Arrows split on hit, dealing damage to multiple targets                            |
| **Archer Tier 2**            | Increased percentage-based bonus damage                                                                     | Increased split arrow damage and number of targets                                 |
| **Archer Tier 3**            | Further increases percentage-based bonus damage                                                             | Further increases split arrow damage and target count                              |
| **Mage - General Traits**    | Low HP, medium movement, medium range; can attack or heal                                                   |                                                                                    |
| **Mage Tier 1 - Offense**    | Light magic: reduces healing received by affected units for a duration (non-stackable)                      | Dark magic: inflicts Corrosion on targets (treated as magic damage, non-stackable) |
| **Mage Tier 2 - Offense**    | Light magic: increased healing reduction and duration                                                       | Dark magic: increased corrosion damage and duration                                |
| **Mage Tier 3 - Offense**    | Light magic: further increases healing reduction and duration                                               | Dark magic: further increases corrosion damage and duration                        |
| **Mage Tier 1 - Healing**    | Light magic: single-target heal with higher healing amount                                                  | Dark magic: single-target heal; increases target’s attack for a short time         |
| **Mage Tier 2 - Healing**    | Light magic: multiple single-target heals with increased healing                                            | Dark magic: attack boost duration increased                                        |
| **Mage Tier 3 - Healing**    | Light magic: group healing with increased effect                                                            | Dark magic: group healing; grants attack boost                                     |
| **Worker - General Traits**  | Low HP, medium movement, melee; can mine and garrison resource buildings                                    |                                                                                    |
| **Worker Tier 1**            | Focused Production: increases resource production efficiency                                                | Focused Conversion: increases resource conversion efficiency                       |
| **Worker Tier 2**            | Further increases production efficiency                                                                     | Further increases conversion efficiency                                            |
| **Worker Tier 3**            | Maximum production efficiency                                                                               | Maximum conversion efficiency                                                      |
| **Cavalry - General Traits** | Medium HP, high movement speed, moderate attack power; reduced damage taken while moving                    |                                                                                    |
| **Cavalry Tier 1**           | Assault: gains more attack power as HP decreases                                                            | Suppression: reduces enemy attack speed                                            |
| **Cavalry Tier 2**           | Increases attack bonus per lost HP                                                                          | Increases attack speed reduction on enemies                                        |
| **Cavalry Tier 3**           | Further increases attack bonus per lost HP                                                                  | Further increases attack speed reduction                                           |

