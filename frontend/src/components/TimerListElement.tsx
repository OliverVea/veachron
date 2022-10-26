import React from 'react';

import Collapse from '@mui/material/Collapse';
import List from '@mui/material/List';
import ListItemText from '@mui/material/ListItemText';
import ListItemButton from '@mui/material/ListItemButton';

import { ListTimersResponse } from '../shared/Api';

interface IProps {
    tree: ListTimersResponse[] | undefined
    indent: number
}

function TimerListElement({ tree, indent = 0 }: IProps): JSX.Element {
    const [open, setOpen] = React.useState(false);

    const handleClick = () => {
        setOpen(!open);
    };

    if (tree === undefined) return <></>
    return (
        <List sx={{ 
            width: 'fit-content', 
            bgcolor: 'background.paper', 
            zIndex: 1000 + indent, 
            mt: 1, 
            padding: 0 }} component="nav">
            {
                tree.map((node, i) => (
                    <div key={i.toString()}>
                        <ListItemButton sx={{
                                margin: 0,
                                padding: 1, 
                                marginLeft: (indent * 1), 
                                color: "#222",
                                width: "fit-content",
                                border: "1px solid #222",
                                borderRadius: 1
                            }} 
                            dense={true}
                            onClick={handleClick}>
                            <ListItemText sx={{
                                padding: 0,
                                margin: 0
                            }}>
                                {node.displayName}: {Number(node.totalTime).toFixed(2)}s ({(Number(node.totalPercentage) * 100).toFixed(1)}%)
                            </ListItemText>
                        </ListItemButton>
                        <Collapse in={open} timeout="auto" unmountOnExit>
                            <TimerListElement tree={node.children} indent={indent + 1} />
                        </Collapse>
                    </div>
                ))
            }
        </List>
    )

}

export default TimerListElement