SLASH_RELOADUI1 = "/rl"
SlashCmdList.RELOADUI = ReloadUI

--lvlPlayer = UnitLevel("player")
--print("Привет, " .. UnitName("player") .. " у вас " .. lvlPlayer .. " уровень!")
--if lvlPlayer == 110 then 
--    print("Поздравляем, вы максимального уровня!")
--end

--local frame = CreateFrame("FRAME");
--frame:RegisterEvent("PLAYER_ENTERING_WORLD");
--
--local function eventHandler(self, event, ...)
-- print("Hello World! Hello " .. event);
--end
--
--frame:SetScript("OnEvent", eventHandler);


------------------------------- UI
--local UIConfig = CreateFrame("Frame", "AAAsfs_BuffFrame", UIParent, "BasicFrameTemplateWithInset");
--UIConfig:SetSize(300, 360);
--UIConfig:SetPoint("CENTER", UIParent, "CENTER");


local frame = CreateFrame("Frame")   

DungeonInfoCollector = {}
local function OnEvent(self, event, ...)
    if event == "LFG_PROPOSAL_SHOW" then
        print("Hello, LFG_PROPOSAL_SHOW is working")
        local proposalExistsDN, typeIDDN, idDN, nameDN, textureDN, roleDN, hasRespondedDN, totalEncountersDN, completedEncountersDN, numMembersDN, isLeaderDN = GetLFGProposal();
        print("Dungeon name = " .. textureDN)
        -- TargetUnit("player");
        
        -- ReloadUI()
--    elseif event == "LFG_PROPOSAL_FAILED" and event=="LFG_PROPOSAL_SUCCEEDED" then
        if event=="LFG_PROPOSAL_SUCCEEDED" then
            tinsert(DungeonInfoCollector,format("%s,%s,%s,%s",date("%m/%d/%y"),date("%H:%M:%S"),UnitName("player"),textureDN))
        end
    end
end

frame:SetScript("OnEvent", OnEvent)
    
frame:RegisterEvent("PLAYER_ENTERING_WORLD")
frame:RegisterEvent("LFG_PROPOSAL_SHOW")