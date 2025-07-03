import * as vscode from 'vscode';

export class TreeViewProvider implements vscode.TreeDataProvider<TreeItem> {
    private _onDidChangeTreeData: vscode.EventEmitter<TreeItem | undefined | null | void> = new vscode.EventEmitter<TreeItem | undefined | null | void>();
    readonly onDidChangeTreeData: vscode.Event<TreeItem | undefined | null | void> = this._onDidChangeTreeData.event;

    getTreeItem(element: TreeItem): vscode.TreeItem {
        return element;
    }

    getChildren(element?: TreeItem): TreeItem[] {
        if (!element) {
            // Root menus
            return [
                new TreeItem('Database', vscode.TreeItemCollapsibleState.Collapsed),
                new TreeItem('Thesaurus', vscode.TreeItemCollapsibleState.Collapsed),
            ];
        }

        if (element.label === 'Database') {
            // Submenu 1 items
            return [
                new TreeItem('Command 1 (No Input)', vscode.TreeItemCollapsibleState.None, {
                    command: 'extension.commandWithoutInput',
                    title: 'Command 1',
                }),
                new TreeItem('Command 2 (With Input)', vscode.TreeItemCollapsibleState.None, {
                    command: 'extension.commandWithInput',
                    title: 'Command 2',
                }),
            ];
        }

        if (element.label === 'Thesaurus') {
            return [
                new TreeItem('Sub-submenu 1', vscode.TreeItemCollapsibleState.Collapsed),
            ];
        }


        

        if (element.label === 'Sub-submenu 1') {
            // Sub-submenu items
            return [
                new TreeItem('Command 3', vscode.TreeItemCollapsibleState.None, {
                    command: 'extension.commandWithoutInput',
                    title: 'Command 3',
                }),
            ];
        }

        return [];
    }
}

class TreeItem extends vscode.TreeItem {
    constructor(
        public readonly label: string,
        public readonly collapsibleState: vscode.TreeItemCollapsibleState,
        public readonly command?: vscode.Command
    ) {
        super(label, collapsibleState);
        this.command = command;
    }
}