## My 2048 Game Logic

graph TD
    Start([Start Game]) --> Grid[Initialize Grid]
    
    Grid --> Action{Choose Action}
    
    %% Play Logic
    Action -->|Move ↑ up/↓ down/← left/→ right| Move[1. Save Undo Snapshot<br/>2. Shift & Merge Tiles<br/>3. Spawn New Tile<br/>4. Clear Redo Stack]
    Move --> Action
    
    %% Undo Logic
    Action -->|Undo| Undo[1. Save Current to Redo<br/>2. Restore Last Snapshot]
    Undo --> Action
    
    %% Redo Logic
    Action -->|Redo| Redo[1. Save Current to Undo<br/>2. Restore Redo Snapshot]
    Redo --> Action
    
    %% Restart Logic
    Action -->|Restart| Start
    
    %% Game Over
    Move -->|No Moves Left| End([Game Over])

    style Start fill:#f9f,stroke:#333
    style Action fill:#fff4dd,stroke:#d4a017
    style End fill:#ffcccb,stroke:#333
    style Grid fill:#bbf,stroke:#333