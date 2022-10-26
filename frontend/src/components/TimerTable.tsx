import React from 'react';

import { ListTimersResponse } from '../shared/Api';

interface IProps {
    tree: ListTimersResponse[] | undefined
    indent: number
}

function TimerTable({tree, indent = 0}: IProps): JSX.Element {
    console.log(tree)
    if (tree === undefined) return <></>
    return <>{
        tree.map((node, _) => (
            <div className="timer-table">
                <div className="timer-info">
                    {indent} {node.displayName}: {Number(node.totalTime).toFixed(2)}s ({(Number(node.totalPercentage) * 100).toFixed(1)}%)
                </div>
                <div className="timer-children">
                    <TimerTable tree={node.children} indent={indent + 1} />
                </div>
            </div>
        ))
    }</>
}

export default TimerTable